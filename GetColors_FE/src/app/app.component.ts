import { Component, ElementRef, Renderer2, ViewChild } from '@angular/core';
import { CrudService } from './crud.service';
import { NgxSpinnerService } from "ngx-spinner";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  blocks :any;
  @ViewChild('topic') topics:ElementRef;

  constructor(private renderer: Renderer2,private crud: CrudService,private spinner: NgxSpinnerService) {
    
   }

  getVal(topic){
    if(topic){
    this.spinner.show();
    this.blocks = [];
    this.crud.fetchColors(topic).subscribe(data => {
      this.blocks = data;
      this.spinner.hide();
      this.topics.nativeElement.value = "";
    });
    }
  }

  getDesign(col){
    return {'backgroundColor': col}
  }
}
