function pltShow() {
  const div = document.querySelector('#plot');
  const img = document.createElement('img');
  svgData = location.hash.slice(1);
  img.src = `data:image/svg+xml;base64,${svgData}`;
  div.appendChild(img);
}
