import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'users-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './list.html',
  styleUrls: ['./list.scss']
})
export class UsersListComponent {
  users = [
    { name: 'Ali', family: 'Seraji' },
    { name: 'Test', family: 'User' }
  ];
}
