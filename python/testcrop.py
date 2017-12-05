from PIL import Image
test="BarHalfGauge.png"
def crop(pfad):
  img = Image.open(pfad)
  img.show()
  box = (150, 180, 670, 470)
  img_region = img.crop(box)
  img_region.save(pfad)
crop(test)
