#include<stdio.h>
#include<stdlib.h>


// 단계 1 :함수 사용 안하는 버전으로 작성하기

// typedef struct Node{
//     struct Node *next;
//     int data;
// }Node;

// int main(){
//     Node *head, *node;

//     node = (Node *) malloc(sizeof(Node));
//     node->data = 10;
//     node->next = NULL;

//     head = node;
//     printf("%d\n",head->data);

//     free(head);
//     return 0;
    
// }



// 단계 2 : 노드 할당하고 초기화하는 부분을 함수로 작성하기


//방법 A : 함수의 리턴 값을 활용하는 방법


// typedef struct Node{ //구조체 Node 정의
//     struct Node *next;
//     int data;
// }Node;

// Node *get_node(){ // 함수 시작
//     Node *node = (Node *) malloc(sizeof(Node)); //노드 할당 및 주소 대입
//     node->data = 10;  //멤버 변수에 값 대입
//     node->next = NULL;  // A. 멤버 변수에 값 대입

//     return node; //node에 저장된 값 리턴
// }

// int main(){
//     Node *head = NULL; //구조체 포인터 변수 선언

//     head = get_node(); // B. 함수 호출 (head에 노드 추가)
    
//     printf("%d\n",head->data); //정상적으로 출력

//     free(head);  //할당받은 메모리 해제

//     return 0;
// }




//방법 B : 이중 포인터를 활용하는 방법
// '변수 head의 주소를 인자로 전달'하여, get_node함수에서 직접 head의 값 변경

// typedef struct Node{
//     struct Node *next;
//     int data;
// }Node;

// void get_node(Node **phead){
//     Node *node = (Node *) malloc( sizeof(Node));
//     node->data = 10;
//     node->next = NULL;

//     *phead = node;
// }

// int main(){
//     Node *head = NULL;

//     get_node( &head);

//     printf("%d\n",head->data);

//     free(head);

//     return 0;

// }

// 방법 C : head를 구조체로 감싸는 방법
// head의 자체의 주소가 아니라 'head를 감싼 구조체의 주소를 전달'하여 , head의 값 변경

// typedef struct Node{
//     struct Node *next;
//     int data;
// }Node;

// typedef struct List{
//     struct Node *head;
// }List;

// void get_node(List *plist){
//     Node *node = (Node *) malloc( sizeof(Node));
//     node->data =10;
//     node->next = NULL;

//     plist->head = node;
// }

// int main(){
//     List list = {NULL};

//     get_node(&list);

//     printf("%d\n", list.head->data);

//     free(list.head);

//     return 0;
// }


// 응용 문제

// n개의 정수를 입력받아, 리스트의 맨 앞에 차례로 추가하는 프로그램을 작성하라.
// 예를 들어, 10,20,30이 입력되면, 최종 리스트 모양은 30 -> 20 -> 10  
// 앞서 설명한 방법으로 함수 작성

typedef struct Node{
    struct Node *next;
    int data;
}Node;

Node *insert_first(Node *head, int data){
    Node *node = (Node *) malloc( sizeof(Node));
    node->data = data;
    node->next = head;

    return node;
}

void print_list(Node *node){
    while(node){
        printf("%d\n",node->data);
        node = node->next;
    }
}

void free_list(Node *node){
    if(node){
        free_list(node->next);
        free(node);
    }
}

int main(void){
    Node *head = NULL;
    int n, data, i;
    char cal;
    int r;
    scanf("%d", &n);

    for(i=0;i<n;++i){
        scanf("%d",&data);
        head = insert_first(head,data);

    }
    print_list(head);
    free_list(head);

    return 0;
}