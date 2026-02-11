from ..domain.block import Block

class BlockchainService:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        new_block = Block(len(self.chain), previous_hash, data)
        self.chain.append(new_block)
        return new_block

    def get_chain(self):
        return self.chain
