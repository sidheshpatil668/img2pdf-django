import os
import uuid
from django.http import FileResponse
from PIL import Image
from django.conf import settings


def convert_images_to_pdf(request):
    if request.method == "POST":
        files = request.FILES.getlist("images")
        if not files:
            return FileResponse(b"Please upload at least one image.", status=400)

        images = []
        try:
            for f in files:
                img = Image.open(f)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                images.append(img)

            # Unique filename
            pdf_name = f"{uuid.uuid4().hex}.pdf"
            pdf_path = os.path.join(settings.MEDIA_ROOT, pdf_name)

            # Ensure media folder exists
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

            # Save PDF
            images[0].save(pdf_path, save_all=True, append_images=images[1:])

            # Return PDF directly as download
            return FileResponse(open(pdf_path, "rb"), as_attachment=True, filename="converted.pdf")

        except Exception as e:
            return FileResponse(f"Error while converting: {e}".encode(), status=500)

    # GET request → show upload form
    from django.shortcuts import render
    return render(request, "converter/index.html")
