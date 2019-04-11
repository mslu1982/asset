
$(function(){
    var start = {
        elem: '#start', //选择ID为START的input
        format: 'YYYY/MM/DD hh:mm:ss', //自动生成的时间格式
        min: laydate.now(), //设定最小日期为当前日期
        max: '2099-06-16 23:59:59', //最大日期
        istime: true, //必须填入时间
        istoday: false,  //是否是当天
        start: laydate.now(0,"YYYY/MM/DD hh:mm:ss"),  //设置开始时间为当前时间
        choose: function(datas){
             end.min = datas; //开始日选好后，重置结束日的最小日期
             end.start = datas //将结束日的初始值设定为开始日
        }
    };