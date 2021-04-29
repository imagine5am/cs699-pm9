/**
* @file
* @author Shivam Sood <ssood@cse.iitb.ac.in>
* @version 1.0
*
* @brief This file contains both the LinkList class and a Node class.
**/

/**
* 
* @author Shivam Sood  
*
* @brief A simple LinkList class 
*
* This is a generic class LinkList class. It contains methods
* to manage the list. The class also contains a driver function
* called main.
**/ 
public class LinkList<T> {
 
    private Node<T> front;
    private Node<T> rear;
     
    /**
    * @brief Insert an item to the front of LinkList.
    * @param item This item is added to the front.
    * @return void
    **/
    public void insertFront(T item){
        //add element at the beginning of the queue
        System.out.println("adding at front: "+item);
        Node<T> nd = new Node<T>();
        nd.setValue(item);
        nd.setNext(front);
        if(front != null) front.setPrev(nd);
        if(front == null) rear = nd;
        front = nd;
    }
    
    /**
    * @brief Insert an item to the rear of LinkList.
    * @param item This item is added to the rear.
    * @return void
    */
    public void insertRear(T item){
        //add element at the end of the queue
        System.out.println("adding at rear: "+item);
        Node<T> nd = new Node<T>();
        nd.setValue(item);
        nd.setPrev(rear);
        if(rear != null) rear.setNext(nd);
        if(rear == null) front = nd;
         
        rear = nd;
    }
    
    /**
    * @brief Removes an item (if present) from the front of LinkList.
    * @return void
    */
    public void removeFront(){
        if(front == null){
            System.out.println("Deque underflow!! unable to remove.");
            return;
        }
        //remove an item from the beginning of the queue
        Node<T> tmpFront = front.getNext();
        if(tmpFront != null) tmpFront.setPrev(null);
        if(tmpFront == null) rear = null;
        System.out.println("removed from front: "+front.getValue());
        front = tmpFront;
    }
     
    /**
    * @brief Removes an item (if present) from the rear of LinkList.
    * @return void
    */
    public void removeRear(){
        if(rear == null){
            System.out.println("Deque underflow!! unable to remove.");
            return;
        }
        //remove an item from the beginning of the queue
        Node<T> tmpRear = rear.getPrev();
        if(tmpRear != null) tmpRear.setNext(null);
        if(tmpRear == null) front = null;
        System.out.println("removed from rear: "+rear.getValue());
        rear = tmpRear;
    }
    
    /**
    * @brief Driver class to demonstrate the LinkList class.
    * @param a[] This can be used to pass arguments. 
    * @return void
    */
    public static void main(String a[]){
        LinkList<Integer> deque = new LinkList<Integer>();
        deque.insertFront(34);
        deque.insertFront(67);
        deque.insertFront(29);
        deque.insertFront(765);
        deque.removeFront();
        deque.removeFront();
        deque.removeFront();
        deque.insertRear(43);
        deque.insertRear(83);
        deque.insertRear(84);
        deque.insertRear(546);
        deque.insertRear(356);
        deque.removeRear();
        deque.removeRear();
        deque.removeRear();
        deque.removeRear();
        deque.removeFront();
        deque.removeFront();
        deque.removeFront();
    }
}

/**
* 
* @author Shivam Sood 
*
* @brief Node class for LinkList
*
* This is a generic Node class. It contains methods
* contains getter and setters for prev and next.
**/  
class Node<T>{
     
    private Node<T> prev;
    private Node<T> next;
    private T value;
    
    /**
    * @brief Getter for prev. 
    * @return Node<t>
    */
    public Node<T> getPrev() {
        return prev;
    }

    /**
    * @brief Setter for prev.
    * @param prev This param is to be set as prev. 
    * @return Node<t>
    */
    public void setPrev(Node<T> prev) {
        this.prev = prev;
    }

    /**
    * @brief Getter for prev. 
    * @return Node<t>
    */
    public Node<T> getNext() {
        return next;
    }

    /**
    * @brief Setter for next.
    * @param next This param is to be set as next. 
    * @return void
    */
    public void setNext(Node<T> next) {
        this.next = next;
    }

    /**
    * @brief Getter for value. 
    * @return T
    */
    public T getValue() {
        return value;
    }

    /**
    * @brief Setter for next.
    * @param value This param is to be set as value. 
    * @return void
    */
    public void setValue(T value) {
        this.value = value;
    }
}