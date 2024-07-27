import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
  cloud_name = 'duwwvifxn',  
  api_key = '242214987592662',  
  api_secret = 'jtvC0YQRbM4KbrlS_RJvp84He7U'  
)

def upload_image(file):
    upload = cloudinary.uploader.upload(file, resource_type = "image")
    return upload['url']
  
def upload_video(file):
    upload = cloudinary.uploader.upload(file, resource_type = "video")
    return upload['url']
