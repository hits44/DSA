class Node:
    def __init__(self,val,key) -> None:
        self.val=val
        self.key=key
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail=Node(0,0)
        self.head.next = self.tail
        self.head.next = None
        self.tail.prev= self.head
        self.tail.next = None


        self.m  = {}
        self.capacity = capacity


    def get(self, key: int) -> int:
        
        if key in self.m:
            #  node to delete 
            loc = self.m[key]
            delnode = loc

            # get value of the node 
            val = delnode.val
            
            # delet it 
            delnodeprev = delnode.prev
            delnodenext = delnode.next
            delnodeprev.next = delnodenext
            delnodenext.prev= delnodeprev

            # add node
            newnodenext = self.head.next
            newnode = Node(val,key)
            self.head.next =newnode
            newnode.prev=self.head
            newnode.next= newnodenext

            self.m[key]= newnode

            return val



    def put(self, key: int, value: int) -> None:

        size = len(self.m)

        if size >= self.capacity:
            # delete lru node' i.e before the tail

            delnode = self.tail.prev
            delkey = delnode.val
            delnodeprev = delnode.prev
            delnodenext = self.tail
            delnodeprev.next = delnodenext
            delnodenext.prev= delnodeprev

            self.m.pop(delkey)

        
        if key in self.m:
            #  node to delete 
            loc = self.m[key]
            delnode = loc
            
            # delet it 
            delnodeprev = delnode.prev
            delnodenext = delnode.next
            delnodeprev.next = delnodenext
            delnodenext.prev= delnodeprev

        # add node
        newnodenext = self.head.next
        newnode = Node(value,key)
        self.head.next =newnode
        newnode.prev=self.head
        newnode.next= newnodenext

        self.m[key] = newnode




        
