function GetRequest(urlStr) {
    if (typeof urlStr == "undefined") {
        var url = decodeURI(location.search); //获取url中"?"符后的字符串
    } else {
        var url = "?" + urlStr.split("?")[1];
    }
    var theRequest = new Object();
    if (url.indexOf("?") != -1) {
        var str = url.substr(1);
        strs = str.split("&");
        for (var i = 0; i < strs.length; i++) {
            theRequest[strs[i].split("=")[0]] = decodeURI(strs[i].split("=")[1]);
        }
    }
    return theRequest.datetime;
}


function appTimeButton() {

    var buttonlist //=[button1,button1,button1,button1]
    $.ajax({
        type: "post",
        async: false,
        url: "/upload/ButtonList",
        dataType: "json",
        success: function (ButtonList) {
            buttonlist = ButtonList;   //请求数据成功的回调函数
        }
    });

    $('#testbutton').append(buttonlist)

}

function OnButtonClick() {
    $('#testbutton').children().on('click', function (event) {
        var $this = $(this);
        var datetime = String($this[0].innerText);
        alert('将要转到 ' + datetime + '的数据');
        var url = '/upload/OutDatatest' + '?datetime=' + datetime
        window.location.replace('/shaderinfo/datatable' + '?datetime=' + datetime);
        return url;
    })


}


function padding() {




    $('#testrange').on('click', function (event) {
        var $this = $(this);
        var value = $this.val();
        $('#astrotext').text(value);
    });

}


$(function () {
    "use strict";

    var thisurl = '/upload/OutDatatest'


    padding();
    appTimeButton();
    OnButtonClick();
    var urldatetime = GetRequest();
    if (typeof urldatetime == "undefined") {
        thisurl = '/upload/OutDatatest';
    } else {
        thisurl += '?datetime=' + urldatetime;
    }


    var thisdata = {
        url: String(thisurl),
        dataSrc: function (result) {
            return result.data.aaData;
        }
    };


    $(document).ready(function () {
        $('#example')
            .DataTable(
                {
                    "paging": true,
                    "iDisplayLength": 10, //默认每页数量
                    //"bPaginate": true, //翻页功能
                    "bLengthChange": true, //改变每页显示数据数量
                    "bFilter": true, //过滤功能
                    "bSort": true, //排序功能
                    "bInfo": true, //页脚信息
                    "bAutoWidth": true, //自动宽度
                    "bRetrieve": true,
                    "processing": true,
                    //"serverSide" : true,//服务器端进行分页处理的意思
                    "bPaginate": true,
                    //"bProcessing": true
                    "ajax": thisdata,
                    columns: [
                        {
                            'data': "id"
                        },
                        {
                            'data': "MaterialName"
                        },
                        {
                            'data': "QualityLevel"
                        },
                        {
                            'data': "ShaderName"
                        },
                        {
                            'data': "WorkRegisters"
                        },
                        {
                            'data': "UniformRegisters"
                        },
                        {
                            'data': "16-bit arithmetic"
                        },
                        {
                            'data': "Total Instruction: FMA"
                        },
                        {
                            'data': "Total Instruction: CVT"
                        },
                        {
                            'data': "Total Instruction: SFU"
                        }
                    ]
                });
    });


    //     $.ajax({
    //     dataType: 'text',
    //     type: "GET",
    //     url: "/upload/OutColumns",
    //     success: function (dataStr) {
    //         var data = eval('(' + dataStr + ')');
    //         $('#timeline').dataTable({
    //             "aaSorting": [[0, "desc"]],
    //             "aaData": data.aaData,
    //             "aoColumns": data.aoColumns,
    //             "bScrollCollapse": true,
    //             "bFilter": false,
    //             "sPaginationType": "full_numbers",
    //             "bJQueryUI": true,
    //             // "aoColumnDefs": data.aoColumnDefs
    //         });
    //     }
    // });
    //


    $(document).ready(function () {
        var table = $('#example2').DataTable({
            lengthChange: false,
            buttons: ['copy', 'excel', 'pdf', 'print']
        });

        table.buttons().container()
            .appendTo('#example2_wrapper .col-md-6:eq(0)');
    });


});