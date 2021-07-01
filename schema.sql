create table if not exists Books
(
    ISBN      VARCHAR  not null
        constraint Books_pk
            primary key,
    title     NVARCHAR not null,
    category  NVARCHAR,
    price     INTEGER default 0,
    author    NVARCHAR,
    publisher NVARCHAR,
    status    INTEGER default 0
);

create unique index if not exists Books_ISBN_uindex
    on Books (ISBN);

create table if not exists Members
(
    ID                INTEGER not null
        constraint Members_pk
            primary key autoincrement,
    name              NVARCHAR,
    age               INTEGER,
    address           NVARCHAR,
    registration_date INTEGER,
    max_credit        INTEGER
);

create unique index if not exists Members_ID_uindex
    on Members (ID);

create table if not exists IssueStatus
(
    issue_id  INTEGER not null
        constraint IssueStatus_pk
            primary key autoincrement,
    date      INTEGER,
    member_id INTEGER
        constraint IssueStatus_Members_ID_fk
            references Members
            on update cascade on delete cascade,
    book_ISBN VARCHAR
        constraint IssueStatus_Books_ISBN_fk
            references Books
            on update cascade on delete cascade
);

create unique index if not exists IssueStatus_issue_id_uindex
    on IssueStatus (issue_id);

create table if not exists ReturnStatus
(
    return_id INTEGER not null
        constraint ReturnStatus_pk
            primary key autoincrement,
    issue_id  INTEGER
        constraint ReturnStatus_IssueStatus_issue_id_fk
            references IssueStatus
            on update cascade on delete cascade,
    date      INTEGER,
    member_id INTEGER
        constraint ReturnStatus_Members_ID_fk
            references Members
            on update cascade on delete cascade,
    book_ISBN VARCHAR
        constraint ReturnStatus_Books_ISBN_fk
            references Books
            on update cascade on delete cascade
);

create unique index if not exists ReturnStatus_return_id_uindex
    on ReturnStatus (return_id);
