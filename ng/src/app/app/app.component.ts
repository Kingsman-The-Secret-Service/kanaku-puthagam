import { Component } from '@angular/core';
import { NbSidebarService } from '@nebular/theme';
import { ToasterConfig } from 'angular2-toaster';

@Component({
  selector: 'app-root',
  template: '<router-outlet></router-outlet>'
})

export class AppComponent {
  title = "Kananku Puthagam"
}

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html'
})

export class ChildComponent {

  	public name = localStorage.getItem('name');
    public menu = mainMenu;
    public userMenu = userMenu;
    public toasterconfig:ToasterConfig = new ToasterConfig({
        animation: "flyRight",
        limit: 5,
        tapToDismiss: true,
        showCloseButton: true,
        newestOnTop: true,
        timeout: 2000,
        positionClass: "toast-top-right",
        preventDuplicates: true,
    });
    

	constructor(private sidebarService: NbSidebarService) {}

	toggleSidebar(): boolean {
		this.sidebarService.toggle(true, 'menu-sidebar');
		return false;
	}

}


import { NbMenuItem } from '@nebular/theme';

const mainMenu: NbMenuItem[] = [
  {
    title: 'Dashboard',
    icon: 'nb-home',
    link: '/',
    home: true,
  },
  {
    title: 'Category',
    icon: 'nb-list',
    link: '/category',
    children: [
      {
        title: 'List',
        link: '/category/list',
      },
      {
        title: 'Create',
        link: '/category/create',
      },
    ],
  }
];

const userMenu: NbMenuItem[]  = [
	{ title: 'View', link: '/profile'},
  { title: 'Edit', link: '/profile/update'},
	{ title: 'Log out', link: '/logout' }
];