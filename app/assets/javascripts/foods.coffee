# Place all the behaviors and hooks related to the matching controller here.
# All this logic will automatically be available in application.js.
# You can use CoffeeScript in this file: http://coffeescript.org/
markersArray = [<%=@all%>]

window.initMap = ->
  map.addListener 'click', (e) ->
    placeMarkerAndPanTo e.latLng, map
    updateFields e.latLng

placeMarkerAndPanTo = (latLng, map) ->
  markersArray.pop().setMap(null) while(markersArray.length)
  marker = new google.maps.Marker
    position: latLng
    map: map

  map.panTo latLng
  markersArray.push marker
