import marshal

def decode_marshal_data(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()  # ফাইল থেকে marshal ডেটা পড়ুন
            decoded_data = marshal.loads(data)  # marshal ডেটা ডিকোড করুন
            return decoded_data
    except Exception as e:
        print(f"Error: {e}")

# ফাইল পাথ দিন যেখানে ফাইলটি আছে
file_path = '/storage/emulated/0/Download/Osint-fb.py'

decoded_data = decode_marshal_data(file_path)

if decoded_data:
    print("Decoded Data:")
    print(decoded_data)
