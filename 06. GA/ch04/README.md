# Thuật toán Genetic Algorithms (giải thuật di truyền)

## Tư tưởng

Nhằm giải thích sự xuất hiện của Hươu cao cổ, Darwin đưa ra giả thiết rằng: “Trong quần thể Hươu vốn đã tồn tại những con Hươu có cổ cao hơn bình thường nhờ gen di truyền và sự đột biến. Trải qua quá trình sinh sống và phát triển, môi trường thay đổi khiến cho thức ăn càng ngày càng khó kiếm hơn, khiến những con Hươu có chiếc cổ cao sẽ chiếm ưu thế sinh tồn hơn. Lâu dần thì thế hệ Hươu mới sẽ được thay bằng những con Hươu cao cổ có khả năng sinh sản và thích nghi với môi trường lớn hơn”.

Dawwin Evolution Theory

Nhìn vào thuyết tiến hóa của Hươu cao cổ này, chúng ta thấy được sự xuất hiện của những thành phần sau:

- Quần thể (population)
- Đột biến (mutation)
- Sinh sản (crossover)
- Chọn lọc tự nhiên (selection)

đây cũng chính là những thành phần trong giải thuật này.

## Thuật toán

1. Lấy dữ liệu bài toán từ người dùng (nhập N quân hậu)
2. Tính lợi ích tối đa mà ta có thể đạt được (N*(N-1)/2 đây là giá trị lớn nhất có thể đạt được)
3. Khởi tạo quần thể ban đầu và giá trị lợi ích cho mỗi cá thể đó trong quần thể (số cá thể theo code là 200 cá thể trong quần thể)
4. Từ quần thể ban đầu chọn ra cá thể có giá trị lợi ích lớn nhất (khởi tạo kết quả cho lời giải)
5. Thực hiện lặp tối đa 1000 lần (số thế hệ mới được sinh ra) cho đến khi tìm được lời giải hay đã đạt tối đa số lần có thể lặp
  - Với mỗi lần lặp (thế hệ mới):
    - Tạo ra quần thể mới (thế hệ mới) dựa trên quần thể củ
      - Chọn cặp cha mẹ (selection parent, roulette_wheel_selection).
      - Thực hiện việc sinh sản (chéo hóa gen) của cặp cha mẹ được chọn (crossover, two_point_crossover).
      - Với một số con được tạo ra sau sinh sản sẽ xuất hiện hiện tượng đột biến gen (mutation, random_reset_mutation).
    - Tính lại giá trị lợi ích cho mỗi cá thể có trong quần thể mới
    - Với quần thể mới ta chọn ra cá thể tốt nhất (giá trị lợi ích cao nhất) so sánh với cá thể đã lưu trước đo và cập nhật lại lời giải
6. Thực hiện hiển thi thông báo kết quả tìm được ra màn hình, có thể là kết quả sau 1000 thế hệ (chưa phải kết quả chính thức).

## Screenshots

![image](https://github.com/nxhawk/MLN/assets/92797788/a5c56a1a-888d-4c98-a259-965e7f6745b6) ![image](https://github.com/nxhawk/MLN/assets/92797788/992b655c-e9cc-43f2-8bda-15253c7d0d17)

![image](https://github.com/nxhawk/MLN/assets/92797788/1d316972-1d21-48f1-810f-0996d3cba820) ![image](https://github.com/nxhawk/MLN/assets/92797788/5be355ae-80cb-4a27-bd20-a3ed4d15929e)

![image](https://github.com/nxhawk/MLN/assets/92797788/19a68507-8afd-4569-b4c4-b00dc5428bdc)



## Tham khảo
[1. Genetic Algorithm - Giải thuật di truyền](https://nerophung.github.io/2020/05/28/genetic-algorithm)
</br>
[2. Learn Genetic Algorithm](https://www.tutorialspoint.com/genetic_algorithms/index.htm)
</br>
[3. Github](https://github.com/abdosharaf9/N-Queens-Project/tree/master)
</br>
