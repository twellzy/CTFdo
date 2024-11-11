class Forensics:
    def __init__(self, filename, flag_begin):
        self.filename = filename
        self.flag_begin = flag_begin
        self.flag_begin_b = flag_begin.encode('utf-8')
        self.flag_length = len(flag_begin)

    def findFlag(self): #finds index of start of flag and returns it, currently returns INT
        flag = b''
        matching_bytes = 1
        counter = 0
        chunk_size = 8192
        file = open(self.filename, "rb")
        while True:
            chunk = file.read(chunk_size)
            if chunk == b"":
                break

            #FIX: if flag is split by chunk_size the loop will detect no flag in the file
            else:
                for byte in chunk:
                    while byte == self.flag_begin_b[0]:
                        if chunk[counter+matching_bytes] == self.flag_begin_b[matching_bytes]:
                            matching_bytes += 1

                        else:
                            break

                        if matching_bytes == self.flag_length:
                            index = counter
                            break

                    matching_bytes = 1
                    counter += 1

                chunk = chunk[index:]

                for i in range(len(chunk)):
                    byte = chunk[i:i+1]

                    if byte == b'}':
                        flag = b''.join([flag,byte])
                        return flag
                    flag = b''.join([flag, byte])



