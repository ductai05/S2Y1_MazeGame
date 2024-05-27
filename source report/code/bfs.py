function BFS(startNode, endNode) // Đưa vào đỉnh bắt đầu và kết thúc
    // Danh sách đỉnh cần duyệt sẽ được đưa vào một hàng đợi không ưu tiên
    openSet = queue()
	  
	  // Khởi tạo mảng 1 chiều visited đánh dấu những đỉnh đã thăm, giá trị khởi tạo là chưa thăm 
	  visited[startNode] = đã thăm
	
    Đưa cặp startNode vào openSet
    while openSet không rỗng:
        currentNode = đỉnh trong openSet có thứ tự vào hàng đợi sớm nhất
        if currentNode == endNode:
            return có tồn tại đường đi từ đỉnh bắt đầu đến đỉnh kết thúc
        Loại bỏ currentNode khỏi openSet
        for each neighbor in các_đỉnh_kề(currentNode) // duyệt các đỉnh kề đỉnh hiện tại
            if currentNode không thể tới được neighbor:
                continue
            visited[neighbor] = đã thăm
            đưa neighbor vào openSet
    return không tồn tại đường đi từ đỉnh bắt đầu đến đỉnh kết thúc