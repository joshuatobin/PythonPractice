# Testing Practices Cheat Sheet

## Testing Libraries and Frameworks

- Jest: Primary testing framework
- Mockito: Mocking library for Java
- PowerMock: Extension of Mockito for advanced mocking

## Mocking and Stubbing Strategies

### Jest Mocks

```javascript
jest.mock('module-name');
const mockFunction = jest.fn();
```

### Mockito Mocks

```java
@Mock
private DependencyClass mockDependency;

when(mockDependency.methodName()).thenReturn(expectedValue);
```

### PowerMock for Static Methods

```java
@RunWith(PowerMockRunner.class)
@PrepareForTest(StaticClass.class)
public class TestClass {
    @Test
    public void testStaticMethod() {
        PowerMockito.mockStatic(StaticClass.class);
        when(StaticClass.staticMethod()).thenReturn(expectedValue);
    }
}
```

## Fake Implementations

### In-Memory Database for Testing

```java
public class InMemoryDatabase implements Database {
    private Map<String, Object> storage = new HashMap<>();

    @Override
    public void save(String key, Object value) {
        storage.put(key, value);
    }

    @Override
    public Object get(String key) {
        return storage.get(key);
    }
}
```

### Fake HTTP Client

```javascript
class FakeHttpClient {
    async get(url) {
        // Return predefined responses based on URL
    }

    async post(url, data) {
        // Simulate post requests
    }
}
```

## Test Structure

### Arrange-Act-Assert Pattern

```java
@Test
public void testFeature() {
    // Arrange
    InputData input = new InputData();
    
    // Act
    Result result = systemUnderTest.process(input);
    
    // Assert
    assertEquals(expectedOutput, result);
}
```

## Test Coverage

- Aim for 80% code coverage
- Use JaCoCo for Java projects
- Use Istanbul for JavaScript projects

## Naming Conventions

- Test classes: `*Test.java` or `*Spec.js`
- Test methods: `test*` or `should*`

## Best Practices

1. One assertion per test method
2. Use descriptive test names
3. Isolate tests (no dependencies between tests)
4. Use setup and teardown methods for common operations

## Integration Tests

- Use `@SpringBootTest` for Spring Boot applications
- Mock external services and use in-memory databases

## Performance Testing

- Use JMeter for load testing
- Implement custom benchmarking for critical methods

## Continuous Integration

- Run tests on every pull request
- Fail builds if tests don't pass or coverage decreases