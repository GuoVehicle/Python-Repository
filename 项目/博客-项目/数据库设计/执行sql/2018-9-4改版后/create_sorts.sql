


use awesome;

grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';


create table sorts (
    `id` varchar(50) not null,
    `class_name` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `user_image` varchar(500) not null,
     `created_at` real not null,
		`updated_at`   real  not  null,
		`updated_user_id`   varchar(50) not null,
		`updated_user_name`  varchar(50)  not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;


