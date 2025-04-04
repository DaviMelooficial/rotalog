const routes = [
  {
    path: '/',
    component: () => import('layouts/AuthLayout.vue'),
    children: [
      { path: '', component: () => import('pages/LoginPage.vue') },
    ],
  },
  {
    path: "/dashboard",
    component: () => import("src/pages/DashboardPage.vue"),
  }
];

export default routes;
