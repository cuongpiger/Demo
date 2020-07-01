$(document).ready(function () {
  $("div.poem-stanza").addClass("highlight");
});

/* 
- Nếu thay vì chúng ta chạy hàm như bên trên, chúng ta chỉ đơn thuần chạy
như thế này: 

```
$("div.poem-stanza").addClass("highlight");
```

Lúc này thì sẽ ko có gì xảy ra cả. Vì sao?, vì mã js sẽ chạy ngay khi trình
duyệt được chạy, lúc bấy giờ chúng ta sẽ element html còn đang dc xử lí và
lúc đó đương nhiên chúng ta sẽ ko có bất kì các element html nào để cho jquery
định dạng cả. Vì vậy:

```
$(document).ready(function () {
  // ... do something
});
```

cho phép chúng ta trì hoàn việc thực thi cũng như lên lịch cho mã js chạy
ngay sau khi các element html được render xong
*/