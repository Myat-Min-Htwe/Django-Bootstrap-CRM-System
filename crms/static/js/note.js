console.log("yoo", 11111);

const sr = ScrollReveal ({
    distance: '80px',
    duration: 1500,
    delay: 450,
    reset: true
  });
  
  
sr.reveal('.link-text',{delay:300, origin: 'top'});
sr.reveal('.searchbox',{delay:150, origin: 'top'});
sr.reveal('.notecard',{delay:400, origin: 'bottom'});