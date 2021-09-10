from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import uuid


# Create your models here.
class ProductDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.id)
        canvas = Image.new(
            "RGB", (qrcode_img.pixel_size, qrcode_img.pixel_size), "white"
        )
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f"qr_code-{self.id}.png"
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super(ProductDetail, self).save(*args, **kwargs)  # Call the real save() method
