import qrcode
from fastapi import FastAPI,Response
import io
from starlette.responses import StreamingResponse
app = FastAPI()

@app.get("/generate_qr")
def generate_qr(text: str):
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    # image_bytes = open(img, "rb").read()
    buf=io.BytesIO()
    img.save(buf)
    buf.seek(0)
    # Return the image as a file response
    return StreamingResponse(buf,media_type="image/jpeg")
