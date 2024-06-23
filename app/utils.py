import cloudinary
import cloudinary.uploader

# Cloudinary configuration
cloudinary.config(
    cloud_name='your_cloud_name',
    api_key='your_api_key',
    api_secret='your_api_secret'
)

def upload_file_to_cloudinary(file_path):
    try:
        response = cloudinary.uploader.upload(file_path, resource_type="auto")
        return response['secure_url']
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None
