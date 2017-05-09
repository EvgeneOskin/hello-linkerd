# hello-linkerd

This is a project to get familiar with [linkerd](https://linkerd.io/).

To get it a bit near to production-like usage, I use
[zipkin](https://github.com/openzipkin/zipkin) for tracing,
a micro-service (**hello**) that forwards linkerd (aka **l5d**) tracking
headers.

## Stack

This is a project with several services:

- a linkerd instance;
- a hello world micro service on top of
  [python-muffin](https://github.com/klen/muffin);
- a zipkin stack (based on [this](https://github.com/openzipkin/docker-zipkin)):

  - a zipkin instance (a tracer for linkerd);
  - a storage for zipkin;
  - dependencies for zipkin;


## Usage

I use [docker-compose](https://docs.docker.com/compose/) to run all services.

```bash
docker-compose build
docker-compsoe up -d
# Visit http://localhost:8080/ - a linkerd route to hello micro-service.
# Visit http://localhost:9411/ - a zipkin ui.
```


## TODO

To get it closer to production-like, it'll nice to add the next features to it:

- routing with service discovery (e.g. [consul](https://www.consul.io/));
- [circuit breaking](https://linkerd.io/features/circuit-breaking/);
- [retries](https://linkerd.io/features/retries-deadlines/);
- [load-balancing](https://linkerd.io/features/load-balancing/).
