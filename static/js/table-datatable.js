$(function () {
    "use strict";

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
                    "ajax": {
                        url: "/upload/OutDatatest",
                        dataSrc: function (result) {
                            //这里result和上面jquery的ajax的代码类似，也是可以得到data.json的数据，但是这样的格式，Datatables不能直接使用，这时候需要在这里处理一下
                            //直接返回Datatables需要的那部分数据即可
                            return result.data.aaData;
                        }
                    },
                    columns: [
                        {
                            data: "id"
                        },
                        {
                            data: "MaterialName"
                        },
                        {
                            data: "QualityLevel"
                        },
                        {
                            data: "ShaderName"
                        },
                        {
                            data: "WorkRegisters"
                        },
                        {
                            data: "UniformRegisters"
                        },
                        {
                            data: "16-bit arithmetic"
                        },
                        {
                            data: "Total Instruction: FMA"
                        },
                        {
                            data: "Total Instruction: CVT"
                        },
                        {
                            data: "Total Instruction: SFU"
                        }
                        ]

                });
    });

    $(document).ready(function () {
        var table = $('#example2').DataTable({
            lengthChange: false,
            buttons: ['copy', 'excel', 'pdf', 'print']
        });

        table.buttons().container()
            .appendTo('#example2_wrapper .col-md-6:eq(0)');
    });


});