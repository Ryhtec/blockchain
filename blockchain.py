'''
RyhtecCoin (RC)

t= transaction
t1: Alice sends rich 2 RC
t2: rich sends naomi 4. 3 RC
t3: Sam sends Jane 3.2 RC

block chain uses sha56

B = block stores info about transaction

B1("AAA",t1,t2,t3) -> sha56 value(76fd89), B2(sha56(76fd89),t4,t5,t6) -> 8923ff

Hash stores info about previous block

RyhtecHash()

'''
import hashlib
hashlib.sha256

class RyhtecCoinBlock:

    # pass hash of the previous block

    def __init__(self,previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        #concantination
        self.block_data = "-".join(transaction_list) + "-"+ previous_block_hash

        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Alice sends 2 RC to Rich"
t2 = "Rich sends 4.3 RC to Naomi"
t3 = "Sam sends 3.2 RC to Jane"
t4 = "Cate sends 4 RC to Edward"
t5 = "Jose sends 1 RC to Jeremy"
t6 = "Jose sends 5 RC to Sam"

initial_block = RyhtecCoinBlock("initial String ", [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block =RyhtecCoinBlock(initial_block.block_hash, [t3,t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block =RyhtecCoinBlock(second_block.block_hash, [t5,t6])
print(third_block.block_data)
print(third_block.block_hash)