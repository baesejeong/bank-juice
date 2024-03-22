<template>
  <div>
    <div id="map" style="width:100%;height:300px;margin-right:20px;"></div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default{
  name : 'KakaoMap',
  data() {
    return {
      map: null,
      positionObj: {},
      isPositionReady: false,
      latitude : 0,
      longtitude : 0,
    };
  },
  props : {
    bankName: String,
  },
  setup() {},
  created() {},
  mounted() {
    if (window.kakao && window.kakao.maps) {
      this.getCurrentPosition()
      this.loadMap()
    } else {
      this.loadScript()
    }
  },
  unmounted() {},
  methods : {
    //현재위치
    getCurrentPosition () {
      if (!navigator.geolocation) {
        // this.setAlert('위치 정보를 찾을 수 없습니다.1')
      } else {
        navigator.geolocation.getCurrentPosition(this.getPositionValue, this.geolocationError)
        this.loadMap()
      }
    },
    getPositionValue (val) {
      this.latitude = val.coords.latitude
      this.longitude = val.coords.longitude
      this.isPositionReady = true
      },
    geolocationError () {
      // this.setAlert('위치 정보를 찾을 수 없습니다.2')
    },
    setAlert (text) {
      alert(text)
    },

    //카카오 map & service 라이브러리 script 작성
    loadScript() {
      const script = document.createElement('script')
      script.src = '//dapi.kakao.com/v2/maps/sdk.js?appkey=fd3f2e818a73b8155daa42867582aeb3&autoload=false&libraries=services,drawing'
      script.onload = () => window.kakao.maps.load(this.loadMap)
      document.head.appendChild(script)
    },
    //지도 불러오기
    loadMap() {
      const container = document.getElementById('map')
      //키워드로 장소 검색
      const ps = new window.kakao.maps.services.Places()
      ps.keywordSearch( this.bankName, this.placeSearchCB, {
        location: new window.kakao.maps.LatLng(this.latitude, this.longitude),
        radius: 5000,
      })
      const options = {
        center: new window.kakao.maps.LatLng(37.566826, 126.570667),
        level: 3
      }
      //지도 그리기
      this.map = new window.kakao.maps.Map(container, options)
      // this.displayMarker()
    },

    //장소 검색 (검색시 위도, 경도 반환)
    placeSearchCB (data, status, pagination) {
      if (status === window.kakao.maps.services.Status.OK) {
        const bounds = new window.kakao.maps.LatLngBounds()
        for (let i = 0; i < data.length ; i++) {
          this.displayMarker(data[i])
          bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x))
        }
        this.map.setBounds(bounds)
      }
    },

    //마커 생성
    displayMarker(place) {
      var marker = new window.kakao.maps.Marker({
        map: this.map,
        position: new window.kakao.maps.LatLng(place.y, place.x) 
      });      
      window.kakao.maps.event.addListener(marker, 'mouseover', ()=> {
          this.infowindow = new window.kakao.maps.InfoWindow({zIndex:1})
          // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
          this.infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
          this.infowindow.open(this.map, marker);
      });
      window.kakao.maps.event.addListener(marker, 'mouseout', ()=> {
          this.infowindow.close();
      });
  },
 }
}
</script>

<style scoped>

</style>
