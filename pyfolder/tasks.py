#import shutil
#try:
#    shutil.make_archive('test','zip','folder')
#except Exception as e:
#    print(e)
#else:
#    print('zipping  done')

# import zipfile
# import os
# os.chdir(r'F:\Suppu\example')
# exampleZip = zipfile.ZipFile('newzip.zip','w')
#
# exampleZip.close()
#
#
# import pyzipper
#
# def encrypt_():
#
#     secret_password = b'your password'
#
#     with pyzipper.AESZipFile('new_test.zip',
#                              'w',
#                              compression=pyzipper.ZIP_LZMA,
#                              encryption=pyzipper.WZ_AES) as zf:
#         zf.setpassword(secret_password)
#         zf.writestr('test.txt', "What ever you do, don't tell anyone!")
#
#     with pyzipper.AESZipFile('new_test.zip') as zf:
#         zf.setpassword(secret_password)
#         my_secrets = zf.read('test.txt')

# from image_shuffler import Shuffler
# image = Shuffler('F:\Suppu\suppu profile.jpg')
# image.shuffle(matrix=(3,3))
# image.show()


# import base64
# from PIL import Image
# from io import BytesIO
# from xlwt import Workbook
# import os
#
# path='F:\Suppu\RSRI -- Rinu Kulhari (RJ)'
# dic_list = os.listdir(path)
# print('dic_list',dic_list)
#
# for image in dic_list:
#     f = os.path.join(path, image)
#     # Workbook is created
#     wb = Workbook()
#
#     # add_sheet is used to create sheet.
#     sheet1 = wb.add_sheet('Sheet 1')
#
#     with open(f, "rb") as image_file:
#         data = base64.b64encode(image_file.read())
#         data1 = str(data)
#         print('data', data1)
#         sheet1.write(1, 0, data1)
#
#     im = Image.open(BytesIO(base64.b64decode(data)))
#     image = str(im)
#     print('image', image)
#     sheet1.write(2, 0, image)
#     wb.save('xlwt image1.xls')
#
# im.show()
#
# im.save('F:\Suppu\photo.jpg', 'PNG')
#
import pywhatkit

pywhatkit.sendwhatmsg("+917708136290",
                      "Geeks For Geeks!",
                      18, 30)
