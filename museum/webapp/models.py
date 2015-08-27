# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

import uuid 

############
import qrcode
import os
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
        

def get_upload_path(instance, filename):
    f, ext = os.path.splitext(filename)
    new_filename = '%s%s' % (uuid.uuid4().hex, ext)
    return os.path.join('uploads',str(uuid.uuid4()), new_filename)


class Image(models.Model):
    img_image = models.ImageField("Imagem", upload_to=get_upload_path)

    img_description = models.CharField(u"Descrição breve", max_length=200, blank=True)
    
    # Generic ForeignKey
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    
    class Meta:
        verbose_name_plural = "Galeria de Imagens"



class Collection(models.Model):
    col_itemname = models.CharField(u"Nome da Peça", max_length = 200, blank = False)
    col_archeological_site = models.CharField(u"Sitio Arqueológico", max_length = 200, blank = False)
    col_description = RedactorField(verbose_name=u'Descrição do Item',
                                                 redactor_options={'lang': 'en', 'focus': 'true'},
                                                 upload_to='tmp/',
                                                 allow_file_upload=True,
                                                 allow_image_upload=True)

    col_origin_date = models.DateField(u"Data de Origem", blank=True, null=True)
    col_discover_date = models.DateField(u"Data de Descoberta", blank=True , null=True)
    
    col_qr_code = models.ImageField(u'QR Code de acesso ',
                                    upload_to='uploads/qr_codes/', blank=True , null=True,
                                    help_text = 'Este item é utilizado pelo app Android para identificação das peças.'
                                    )
    col_images_galery = generic.GenericRelation(Image)
    
    def image_thumb(self):
        return '<img src="/media/%s" width="30" height="30" />' % (self.col_qr_code)
    image_thumb.allow_tags = True
    image_thumb.short_description = 'Download QR Code'

    def __unicode__(self):
        return self.col_itemname
    
    class Meta:
        verbose_name = u"Acervo"
        verbose_name_plural = u"Acervos"


    def save(self, *args, **kwargs):
        '''Overide save to attach qrcode for each save '''

        #TODO - dont create new qrcode when edit
        uuid_hash = str(uuid.uuid4())
        img = qrcode.make("{}".format(uuid_hash))

        temp_handle = StringIO()
        img.save(temp_handle, 'png')
        temp_handle.seek(0)

        suf = SimpleUploadedFile(uuid_hash,
                temp_handle.read(), content_type='image/png')
        self.col_qr_code.save(suf.name+'.png', suf, save=False)

        super(Collection, self).save(*args, **kwargs)