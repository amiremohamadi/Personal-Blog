window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    document.getElementById("header").style.lineHeight = "50px";
  } else {
    document.getElementById("header").style.lineHeight = "80px";
  }
}
