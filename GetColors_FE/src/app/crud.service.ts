import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class CrudService {
  hostName = 'http://127.0.0.1:5000/colors/'
  constructor(private http: HttpClient) { }

  public fetchColors(data) {
    return this.http.get(this.hostName+data);
  }
}
