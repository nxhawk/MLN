# Huấn luyện rắn trong snake game với mạng nơ-ron và thuật toán di truyền

# Mạng nơ-ron
![image](https://github.com/nxhawk/MLN/blob/master/06.%20GA/SnakeAI/NeutronNetworking.png)

- `INPUTS`: gồm 6 node với ý nghĩa lần lượt là
  + 5 bước gần nhất theo hướng hiện tại có an toàn không, có thể mang các giá trị sau (0: không có bước an toàn, 0.2: 1 bước tiếp không an toàn , 0.4: tương tự, 0.6, 0.8, 1) với ý nghĩa độ an toàn tăng dần
  + 5 bước gần nhất theo hướng trái (tính theo hướng hiện tại) giá trị tương tự như trên
  + 5 bước gần nhất theo hướng phải (tính theo hướng hiện tại) giá trị tương tự như trên
  + Đi theo hướng hiện tại lại gần Food không (0: không, 1: có)
  + Food nằm bên trái con rắn (xét theo hướng hiện tại; 0: không, 1: có)
  + Food nằm bên phải con rắn (xét theo hướng hiện tại; 0: không, 1: có) 
- `HIDDEN LAYER`: 10->20->10: node cho mỗi lớp, weight khởi tạo ngẫu nhiên (0->1), dùng hàm ReLU làm active function (fully connected layer)
- `OUTPUTS`: gồm 3 node, đầu tiên dùng hàm softmax để đưa giá trị 3 node về dạng xác suất

Max node in OUTPUTS sẽ là kết quả dự đoán bước tiếp theo rắn nên đi (node 1: đi tiếp hướng cũ, node 2: rẽ trái, node 3: rẽ phải)

# Genetic Algorithm
Thay vì dùng `backpropagation` để tìm phương án tối ưu ta dùng thuật toán di truyền để tìm các weight tối ưu nhất cho mạng nơ-ron ở trên
- Với population là 50 cho 1 thế hệ
- One posint crossover
- Mutation

# Main source
[Source Code](https://github.com/kairess/genetic_snake/tree/master)







