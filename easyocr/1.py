import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('as.jpg', detail=0)