CREATE DATABASE transportadora;
GRANT ALL PRIVILEGES ON DATABASE transportadora TO postgres;

\connect transportadora;

CREATE TABLE clientes (
  id NUMERIC PRIMARY KEY,
  nome CHARACTER VARYING (255),
  endereco CHARACTER VARYING (255),
  cidade CHARACTER VARYING (255),
  estado CHAR (2)
);

CREATE TABLE pedidos (
  id SERIAL PRIMARY KEY,
  data_criacao DATE,
  id_cliente NUMERIC
);

CREATE TABLE entregas (
  id SERIAL PRIMARY KEY,
  status CHARACTER VARYING (255),
  id_pedido NUMERIC
);


INSERT INTO clientes (id, nome, endereco, cidade, estado)
VALUES
  (1,	'Pedro Augusto da Rocha',	'Rua Pedro Carlos Hoffman',	'Porto Alegre',	'RS'),
  (2,	'Antonio Carlos Mamel',	'Av. Pinheiros', 'Belo Horizonte',	'MG'),
  (3,	'Luiza Augusta Mhor',	'Rua Salto Grande',	'Niteroi',	'RJ'),
  (4,	'Jane Ester',	'Av 7 de setembro',	'Erechim',	'RS'),
  (5, 'Marcos Antônio dos Santos',	'Av Farrapos',	'Porto Alegre',	'RS');


INSERT INTO pedidos (data_criacao, id_cliente)
VALUES
  ('2022-01-01 15:34:34', 2),
  ('2022-01-03 17:12:00', 3),
  ('2022-01-02 08:24:27', 5),
  ('2022-01-02 06:51:16', 1),
  ('2022-01-05 10:03:59', 4);


INSERT INTO entregas (status, id_pedido)
VALUES
  ('Em transito', 2),
  ('Em processamento', 3),
  ('Em transito', 1),
  ('Em transito', 4),
  ('Em transito', 5);
