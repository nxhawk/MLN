# Thuật toán Genetic Algorithms (giải thuật di truyền)

## Tư tưởng

Nhằm giải thích sự xuất hiện của Hươu cao cổ, Darwin đưa ra giả thiết rằng: “Trong quần thể Hươu vốn đã tồn tại những con Hươu có cổ cao hơn bình thường nhờ gen di truyền và sự đột biến. Trải qua quá trình sinh sống và phát triển, môi trường thay đổi khiến cho thức ăn càng ngày càng khó kiếm hơn, khiến những con Hươu có chiếc cổ cao sẽ chiếm ưu thế sinh tồn hơn. Lâu dần thì thế hệ Hươu mới sẽ được thay bằng những con Hươu cao cổ có khả năng sinh sản và thích nghi với môi trường lớn hơn” - Dawwin Evolution Theory.

Nhìn vào thuyết tiến hóa của Hươu cao cổ này, chúng ta thấy được sự xuất hiện của những thành phần sau:

- Quần thể (population)
- Đột biến (mutation)
- Sinh sản (crossover)
- Chọn lọc tự nhiên (survivor selection)

đây cũng chính là những thành phần trong giải thuật này.

## Thuật toán trong quá trình tạo quần thể mới
1. Chọn cặp cha mẹ cho chúng giao phối với nhau(Parent Selection)
   - Roulette Wheel Selection: Các cá thể trong quần thể sẽ được chọn ngẫu nhiên theo tỉ lệ đóng góp vào lợi ích của quần thể
   
     ![image](https://github.com/nxhawk/MLN/assets/92797788/35a74533-3a4c-4a6f-8ff9-45b87a741de9)
   - Stochastic Universal Sampling (SUS): Giống như Roulette Wheel Selection nhưng chọn nhiều lần với điểm mốc vòng quay là ngẫu nhiên
   - Tournament Selection: Chọn ra ngẫu nhiên K cá thể trong quần thể, từ K cá thể được chọn ta chọn ra cá thể có giá trị lợi ích lớn nhất để làm parent 
   - Rank Selection: thường sử dụng khi các cá thể trong quần thể có giá trị lợi ích gần nhau (xảy ra ở các thế hệ gần cuối có thể tạo), ta sắp xếp theo giá trị lợi ích giảm dần, với mỗi cá thể sẽ có một rank chọn ra cá thể có tổng rank ngẫu nhiên
   - Random Selection: chọn ngẫu nhiên một cá thể bất kì trong quần thể làm cha mẹ (không phụ thuộc vào giá trị lợi ích của nó, ít được dùng).

2.  Sinh sản cá thể mới (crossover)
    - One Point Crossover: chọn ra một điểm ngẫu nhiên trên nhiễm sắc thể của bố và mẹ, thế hệ con sẽ kế thừa 1 phần gen của bố và 1 phần của mẹ theo đúng thứ tự
   
       ![image](https://github.com/nxhawk/MLN/assets/92797788/59b571cf-e410-42b4-b353-246039c2b431)
    - Multi Point Crossover: chọn ra N điểm ngẫu nhiên trên nhiễm sắc thể của bố và mẹ, thế hệ con sẽ kế thừa 1 phần gen của bố và 1 phần của mẹ theo đúng thứ tự
     
       ![image](https://github.com/nxhawk/MLN/assets/92797788/fbac988b-0ca3-458d-a98d-2448f75b769e)

    - Uniform Crossover: Với lần lượt từng gên trong nhiễm sắc thể của bố và mẹ thể hệ con được tạo ngẫu nhiên bằng việc kế thừa gen của bố hoặc mẹ ở từng vị trí

       ![image](https://github.com/nxhawk/MLN/assets/92797788/613baa2c-7689-42e1-8744-67bd34210717)
       
 3. Cá thể mới có thể xảy ra hiện tượng đột biến (mutation):
    - Bit Flip Mutation: sử dụng với nhiễm sắc thể chỉ chứa các gen có giá trị (0, 1), nó sẽ lật một bit nào đó trong bộ gen
    - Random Resetting: một giá trị ngẫu nhiên trong tập các giá trị có thể gán cho gen sẽ được gán cho một gen ngẫu nhiên nào đó của nhiễm sắc thể
    - Swap Mutation: chọn ngẫu nhiên hai gen bất kì trong nhiễm sắc thể và hoán đổi giá trị của chúng cho nhau
    - Scramble Mutation: chọn ngẫu nhiên một đoạn gen trong nhiễm sắc thể rồi hoán đổi ngẫu nhiên vị trí của các gen trong đoạn được chọn

       ![image](https://github.com/nxhawk/MLN/assets/92797788/7c775c6a-2cd4-4f76-9508-7a5ae0cce424)
    - Inversion Mutation: chọn ngẫu nhiên một đoạn gen trong nhiễm sắc thể rồi dảo ngược vị trí của các gen trong đoạn được chọn

       ![image](https://github.com/nxhawk/MLN/assets/92797788/15b80917-f4ee-45ef-bd67-4b0a0e64c40f)

  4. Chọn lọc tự nhiên quần thể (Survivor Selection):
     - Age Based Selection: những cá thể già (đã tồn tại qua nhiều thế hệ) sẽ bị loại bỏ ra khỏi quần thể (không quan tâm đến giá trị lợi ích của nó trong quần thể mà quan tâm đến số lượng thế hệ mà cá thể đó đã tồn tại) để thay bằng cá thể mới
     - Fitness Based Selection: Những cá thể có giá trị lợi ích nhỏ sẽ bị loại bỏ ra khỏi quần thể để thay bằng cá thể mới.  
 
## Lời giải

1. Lấy dữ liệu bài toán từ người dùng (nhập N quân hậu)
2. Tính lợi ích tối đa mà ta có thể đạt được (N*(N-1)/2 đây là giá trị lớn nhất có thể đạt được)
3. Khởi tạo quần thể ban đầu và giá trị lợi ích cho mỗi cá thể đó trong quần thể (số cá thể theo code là 200 cá thể trong quần thể)
4. Từ quần thể ban đầu chọn ra cá thể có giá trị lợi ích lớn nhất (khởi tạo kết quả cho lời giải)
5. Thực hiện lặp tối đa 1000 lần (số thế hệ mới được sinh ra) cho đến khi tìm được lời giải hay đã đạt tối đa số lần có thể lặp
  - Với mỗi lần lặp (thế hệ mới):
    - Tạo ra quần thể mới (thế hệ mới) dựa trên quần thể củ
      - Chọn cặp cha mẹ (parent selection, use roulette_wheel_selection).
      - Thực hiện việc sinh sản (chéo hóa gen) của cặp cha mẹ được chọn (crossover, use two_point_crossover).
      - Với một số con được tạo ra sau sinh sản sẽ xuất hiện hiện tượng đột biến gen (mutation, use random_reset_mutation).
      - Ngoài ra còn có việc chọn lọc tự nhiên xảy ra trong quần thể (survivor selection, không được áp dụng trong lời giải)
    - Tính lại giá trị lợi ích cho mỗi cá thể có trong quần thể mới
    - Với quần thể mới ta chọn ra cá thể tốt nhất (giá trị lợi ích cao nhất) so sánh với cá thể đã lưu trước đó và cập nhật lại lời giải
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
