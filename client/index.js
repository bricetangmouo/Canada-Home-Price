function onPageLoad(){
    console.log("document loaded")
    var url = "http://127.0.0.1:5000/get_name_element"
    $.get(url, function(data, status){
        console.log("got response for get_location_names request")
        if(data){
            var province = data.province
            var city = data.city
            var home_type = data.home_type
            var smoking_permission = data.smoking_permission
            var uiProvince = document.getElementById('uiProvince')
            var uiCity = document.getElementById('uiCity')
            var uiHomeType = document.getElementById('uiHomeType')
            var uiSmokingPermission = document.getElementById('uiSmokingPermission')

            $('#uiProvince').empty()
            $('#uiCity').empty()
            $('#uiHomeType').empty()
            $('#uiSmokingPermission').empty()

            for(var i in province){
                var opt = new Option(province[i])
                $('#uiProvince').append(opt)
            }

            for(var i in city){
                var opt = new Option(city[i])
                $('#uiCity').append(opt)
            }

            for(var i in home_type){
                var opt = new Option(home_type[i])
                $('#uiHomeType').append(opt)
            }

            for(var i in smoking_permission){
                var opt = new Option(smoking_permission[i])
                $('#uiSmokingPermission').append(opt)
            }
        }
    })
}

window.onload = onPageLoad