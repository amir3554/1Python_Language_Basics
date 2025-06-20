data = [['Rami', 'Sara', 'Nada', 'Mhamad', 'Salem'], 50, 60, 'rami',('ahmed', 'radhi')]

def recur(n =0):
    if n >= len(data):
        return data[-1]
    else:
        print(data[n] )
        recur(n +1)

recur()

 
def print_data(data):
    if not data : return
    if type(data[0]) == list or type(data[0]) == tuple:
        print_data(data[0])
    else:
        print(data[0])
    return print_data(data[1:])

print_data(data)
 