# Decision Tree Classification in Python

## The Decision Tree Algorithm

### 1. Cây quyết định là gì?
- Cây quyết định là cây mà mỗi nút biểu diễn một đặc trưng (tính chất), mỗi nhánh (branch) biểu diễn một quy luật (rule) và mỗi lá biểu biễn một kết quả (giá trị cụ thể hay một nhánh tiếp tục).

![image](https://user-images.githubusercontent.com/92797788/235626543-983fea90-83c3-4692-aefe-a60e61def1a2.png)

- Nút trên cùng trong cây quyết định được gọi là nút gốc. Nó học cách phân vùng trên cơ sở giá trị thuộc tính. Nó phân vùng cây theo cách đệ quy được gọi là phân vùng đệ quy. Cấu trúc giống như lưu đồ bên dưới giúp bạn ra quyết định. Nó trực quan hóa dễ dàng bắt chước suy nghĩ ở cấp độ con người. Đó là lý do tại sao cây quyết định rất dễ hiểu và diễn giải.

![image](https://user-images.githubusercontent.com/92797788/235626666-31691d03-9ac5-4229-8bda-624da8e1fb27.png)


### 2. Xây dựng một cây quyết định như thế nào?
Ý tưởng cơ bản để xây dựng cây quyết định như sau:
  1. Select the best attribute using Attribute Selection Measures (ASM) to split the records.
  2. Make that attribute a decision node and breaks the dataset into smaller subsets.
  3. Start tree building by repeating this process recursively for each child until one of the conditions will match:
      * All the tuples belong to the same attribute value.
      * There are no more remaining attributes.
      * There are no more instances.

  ![image](https://user-images.githubusercontent.com/92797788/235628307-f01d9829-9d9b-4b97-9134-c3785362bb05.png) 

Một vài thuật toán dùng để xây dựng cây quyết định thường dùng:
  1. CART (Classification and Regression Trees) → dùng Gini Index(Classification) để kiểm tra.
  2. ID3 (Iterative Dichotomiser 3) → dùng Entropy function và Information gain để kiểm tra.

### 3. Dữ liệu dùng để xây dựng cây quyết định trong bài
  [Kaggle dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

### 4. Tài liệu tham khảo
  [1. Entropy and Gini index](https://viblo.asia/p/cay-quyet-dinh-decision-tree-RnB5pXWJ5PG)
  </br>
  [2. Python Decision Tree Classification](https://www.datacamp.com/tutorial/decision-tree-classification-python)
  </br>
  [3. Python | Decision tree implementation](https://www.geeksforgeeks.org/decision-tree-implementation-python)
  
  
  
  
  


