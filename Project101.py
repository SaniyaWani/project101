import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = '2USbGB4Z7rsAAAAAAAAAAZ-g8DhEQaPIPlL56GdvnvkNt7G0sW043q1y_Scyy7UQ'
    transferData = TransferData(access_token)

    file_from = input("enter file you want to transfer to dropbox")
    file_to = input("enter file path you want to transfer to dropbox")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)


main()

        