window.onload=function(){
				const arrowRs=document.getElementsByClassName('arrowR');
				const arrowLs=document.getElementsByClassName('arrowL');
				
				const panelRs=document.getElementsByClassName('panelR');
				const panelLs=document.getElementsByClassName('panelL');
				
				for(let i=0;i<arrowRs.length;i++){
					arrowRs[i].onclick=function(){
						console.log(11);
						panelRs[i].classList.add('toRight');
						
					}
					
					arrowLs[i].onclick=function(){
						console.log(11);
						panelLs[i].classList.add('toLeft');
						
					}
					
				}
				

				
			}

// var panelR=document.getElementsByClassName('panelR');
// var panelL=document.getElementsByClassName('panelL');

// function toRight(){
// 	console.log(11);
// 	for(panelR:panelR){
// 		panelR.classList.add('toRight');
// 	}
	
	
// }