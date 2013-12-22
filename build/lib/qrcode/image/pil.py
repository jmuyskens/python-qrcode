# Try to import PIL in either of the two ways it can be installed.
try:
    from PIL import Image, ImageDraw
except ImportError:
    import Image
    import ImageDraw

from qrcode.image import base


class PilImage(base.BaseImage):
    """
    PIL image builder, default format is PNG.
    """
    kind = "PNG"

    def new_image(self, rgba_color, **kwargs):
        img = Image.new('RGBA', (self.pixel_size, self.pixel_size), rgba_color)
        self._idr = ImageDraw.Draw(img)
        return img

    def drawrect(self, row, col, color):
        box = self.pixel_box(row, col)
        self._idr.rectangle(box, fill=color)

    def save(self, stream, kind=None):
        if kind is None:
            kind = self.kind
        self._img.save(stream, kind)

    def __getattr__(self, name):
        return getattr(self._img, name)
