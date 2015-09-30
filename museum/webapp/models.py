# -*- coding: utf-8 -*-
from django.db import models
from redactor.fields import RedactorField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.sites.models import Site
import uuid 

############
import qrcode
import os
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
        
from geoposition.fields import GeopositionField

def get_upload_path(instance, filename):
    print instance, filename
    f, ext = os.path.splitext(filename)
    new_filename = '%s%s' % (uuid.uuid4().hex, ext)
    return os.path.join('uploads',str(uuid.uuid4()), new_filename)


class Image(models.Model):
    img_image = models.ImageField("Imagem", upload_to=get_upload_path)
    img_thumb = models.ImageField(upload_to=get_upload_path, blank=True, null=True)

    img_description = models.CharField(u"Descrição breve", max_length=200, blank=True)
    
    # Generic ForeignKey
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey()
    
    def create_thumbnail(self):
         
         if not self.img_image:
             return

         from PIL import Image
         from cStringIO import StringIO
         from django.core.files.uploadedfile import SimpleUploadedFile
         import os

         # Set our max thumbnail size in a tuple (max width, max height)
         THUMBNAIL_SIZE = (200,200)

         DJANGO_TYPE = self.img_image.file.content_type

         if DJANGO_TYPE == 'image/jpeg':
             PIL_TYPE = 'jpeg'
             FILE_EXTENSION = 'jpg'
         elif DJANGO_TYPE == 'image/png':
             PIL_TYPE = 'png'
             FILE_EXTENSION = 'png'

         # Open original photo which we want to thumbnail using PIL's Image
         image = Image.open(StringIO(self.img_image.read()))

         image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

         # Save the thumbnail
         temp_handle = StringIO()
         image.save(temp_handle, PIL_TYPE)
         temp_handle.seek(0)

         # Save image to a SimpleUploadedFile which can be saved into
         # ImageField
         suf = SimpleUploadedFile(os.path.split(self.img_image.name)[-1],
                 temp_handle.read(), content_type=DJANGO_TYPE)
         # Save SimpleUploadedFile into image field
         self.img_thumb.save('%s_thumbnail.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False)

    def save(self):
        # create a thumbnail
        self.create_thumbnail()
        super(Image, self).save()
    
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
    
    col_uuid = models.CharField(max_length = 200, blank = False,editable=False)
    col_qr_code = models.ImageField(u'QR Code de acesso ',editable=False,
                                    upload_to='uploads/qr_codes/', blank=True , null=True,
                                    help_text = 'Este item é utilizado pelo app Android para identificação das peças.'
                                    )
    col_position = GeopositionField()

    col_images_galery = generic.GenericRelation(Image)
        
    def image_thumb(self):
        return '<a href="/media/%s" target="blank"><img src="/media/%s" width="30" height="30" /> Imprimir</a>' % (self.col_qr_code,self.col_qr_code)
    
    image_thumb.allow_tags = True
    image_thumb.short_description = 'Download QR Code'


    def __unicode__(self):
        return self.col_itemname
    
    class Meta:
        verbose_name = u"Acervo"
        verbose_name_plural = u"Acervos"


    def save(self, *args, **kwargs):
        '''Overide save to attach qrcode for each save '''
        if not self.pk:
            site_url = Site.objects.get_current()

            #     #TODO - dont create new qrcode when edit
            uuid_hash = str(uuid.uuid4())
            
            img = qrcode.make("{}/api/{}".format(site_url,uuid_hash))

            temp_handle = StringIO()
            img.save(temp_handle, 'png')
            temp_handle.seek(0)

            suf = SimpleUploadedFile(uuid_hash,
                    temp_handle.read(), content_type='image/png')
            self.col_qr_code.save(suf.name+'.png', suf, save=False)
            self.col_uuid = uuid_hash
            super(Collection, self).save(*args, **kwargs)