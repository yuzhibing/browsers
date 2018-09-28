from job import db

class ud_transaction_recods_addr(db.Model):
    __tablename__ = 'ud_transaction_recods_addr'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=True)
    current_date = db.Column(db.TIMESTAMP(True), nullable=True)
    ud_transaction_recods_voutid = db.Column(db.Integer, nullable=True)

    def __init__(self, address):
        self.address = address

    def __repr__(self):
        return '<ud_transaction_recods_addr %r>'

class ud_transaction_recods_vout(db.Model):
    __tablename__ = 'ud_transaction_recods_vout'
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=True)
    txid = db.Column(db.String(True), nullable=True)
    value = db.Column(db.Float, nullable=True)
    n = db.Column(db.Integer, nullable=True)
    ud_transaction_recordsid = db.Column(db.Integer, nullable=True)
    type = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(100), nullable=True)
    mined_time = db.Column(db.TIMESTAMP(True), nullable=True)
    has_vin = db.Column(db.String(100), nullable=True)
    coinbase = db.Column(db.String(100), nullable=True)

    def __init__(self, height):
        self.height = height

    def __repr__(self):
        return '<ud_transaction_recods_vout %r>'

class ud_transaction_recods_vin(db.Model):
    __tablename__ = 'ud_transaction_recods_vin'
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=True)
    txid = db.Column(db.String(True), nullable=True)
    vout = db.Column(db.Integer, nullable=True)
    vin_txid = db.Column(db.String(100), nullable=True)
    ud_transaction_recordsid = db.Column(db.Integer, nullable=True)
    coinbase = db.Column(db.String(100), nullable=True)


    def __init__(self, height):
        self.height = height

    def __repr__(self):
        return '<ud_transaction_recods_vin %r>'

class ud_transaction_records(db.Model):
    __tablename__ = 'ud_transaction_records'
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=True)
    tx_id = db.Column(db.String(True), nullable=True)
    confirmations = db.Column(db.Integer, nullable=True)
    time = db.Column(db.Integer, nullable=True)
    blocktime = db.Column(db.Integer, nullable=True)
    version = db.Column(db.Integer, nullable=True)
    fees = db.Column(db.Float, nullable=True)
    ud_blockid = db.Column(db.Integer, nullable=True)

    def __init__(self,height):
        self.height = height

    def __repr__(self):
        return '<ud_transaction_records %r>'

class udBlock(db.Model):
    __tablename__ = 'ud_block'
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=True)
    mined_by = db.Column(db.TIMESTAMP(True), nullable=False)
    difficulty = db.Column(db.Float, nullable=True)
    transactions_number = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.TIMESTAMP(True), nullable=True)
    Size = db.Column(db.Integer, nullable=True)
    Bits = db.Column(db.String(10), nullable=True)
    Block_reward = db.Column(db.Float, nullable=True)
    Previous_Block = db.Column(db.String(100), nullable=True)
    Next_Block = db.Column(db.String(100), nullable=True)
    BlockHash = db.Column(db.String(100), nullable=True)

    def __init__(self,height, mined_by, difficulty, transactions_number, timestamp, size, bits, block_reward, previous_block, next_block, blockHash):
        self.height = height
        self. mined_by=mined_by
        self.difficulty=difficulty
        self.transactions_number=transactions_number
        self.timestamp=timestamp
        self.size=size
        self.bits=bits
        self.block_reward=bits
        self.previous_block=previous_block
        self.next_block=next_block
        self.blockHash=blockHash

    def __repr__(self):
        return '<ud_block %r>'


class ud_trans_address(db.Model):
    __tablename__ ='ud_trans_address'
    id = db.Column(db.Integer, primary_key=True)
    ut_num = db.Column(db.Integer, nullable=True)
    ut_balance_num = db.Column(db.Integer,nullable=True)
    trans_num = db.Column(db.Integer,nullable=True)
    address_num = db.Column(db.Integer,nullable=True)
    create_date = db.Column(db.TIMESTAMP(True),nullable=False)

    def __repr__(self):
        return '<ud_trans_address %r>'

    def __init__(self,ut_num,ut_balance_num,trans_num,address_num,create_date):
        self.ut_num = ut_num
        self.ut_balance_num = ut_balance_num
        self.trans_num = trans_num
        self.address_num = address_num
        self.create_date = create_date