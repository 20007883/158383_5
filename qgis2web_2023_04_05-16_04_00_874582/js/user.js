$(document).ready(function() {
    $('#user-form').submit(function(event) {
      // 防止表单默认提交行为
      event.preventDefault();
  
      // 获取表单中的数据
      var formData = {
        'username': $('input[name=username]').val(),
        'password': $('input[name=password]').val(),
        'email': $('input[name=email]').val(),
        'phone': $('input[name=phone]').val(),
        'school': $('input[name=school]').val(),
        'note': $('input[name=note]').val()
      };
  
      // 发送ajax请求
      $.ajax({
        type: 'POST',
        url: '/data/add_user',
        data: formData,
        dataType: 'json',
        encode: true
      })
      .done(function(data) {
        console.log(data);
      })
      .fail(function(data) {
        console.log(data);
      });
    });
  });