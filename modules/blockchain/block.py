def block(index, timestamp, data, previousHash = ''):
    def calculate_hash():
        out = str(index) + str(timestamp) + str(data) + str(previousHash)
        return hashlib.sha3_256(out.encode()).hexdigest()