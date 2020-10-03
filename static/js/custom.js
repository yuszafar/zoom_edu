/*=============================================================
    Authour URI: www.binarytheme.com
    License: Commons Attribution 3.0

    http://creativecommons.org/licenses/by/3.0/

    100% Free To use For Personal And Commercial Use.
    IN EXCHANGE JUST GIVE US CREDITS AND TELL YOUR FRIENDS ABOUT US
   
    ========================================================  */

(function ($) {
    "use strict";
    var mainApp = {
        slide_fun: function () {

            $('#carousel-example').carousel({
                interval: 3000 // THIS TIME IS IN MILLI SECONDS
            })

        },
        dataTable_fun: function () {

            $('#dataTables-example').dataTable(
                {
                    pageLength: 15,
                    ordering: false,
                    lengthChange: false,
                    oLanguage: {
                        sSearch: "<i class=\"fa fa-search \">",

                    },
                }
            );
            $('#lesson_info_table').dataTable(
                {
                    pageLength: 15,
                    ordering: true,
                    lengthChange: false,
                    oLanguage: {
                        sSearch: "<i class=\"fa fa-search \">",

                    },


                }
            );

        },

        custom_fun: function () {
            /*====================================
             WRITE YOUR   SCRIPTS  BELOW
            ======================================*/


        },

    }


    $(document).ready(function () {
        mainApp.slide_fun();
        mainApp.dataTable_fun();
        mainApp.custom_fun();
    });
}(jQuery));


