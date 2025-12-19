import { inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { signal } from '@angular/core';

const BASE_URL = 'http://localhost:8000/users/users';

export class UsersApi {
  private http = inject(HttpClient);

  users = signal<any[]>([]);

  loadUsers() {
    this.http.get<any[]>(BASE_URL).subscribe(res => {
      this.users.set(res);
    });
  }

  createUser(data: any) {
    return this.http.post(BASE_URL, data);
  }

  getUser(id: number) {
    return this.http.get(`${BASE_URL}/${id}`);
  }

  updateUser(id: number, data: any) {
    return this.http.put(`${BASE_URL}/${id}`, data);
  }

  deleteUser(id: number) {
    return this.http.delete(`${BASE_URL}/${id}`);
  }
}
