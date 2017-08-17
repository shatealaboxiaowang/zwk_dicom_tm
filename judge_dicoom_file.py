def is_dicom_file(filename):
    if 'DS_Store' not in filename and 'DICOMDIR' not in filename and 'jpg' not in  filename:
        file_stream = open(filename, 'rb')
        file_stream.seek(128)
        data = file_stream.read(4)
        file_stream.close()
        if data == b'DICM':
            return True
        return False