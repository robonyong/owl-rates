function isObject(obj) {
  return (!!obj) && (obj.constructor === Object);
}

function isArray(obj) {
  return (!!obj) && (obj.constructor === Array);
}

export function snakeToCamel(obj) {
  if(!isObject(obj) && !isArray(obj)) return obj;
  if(isArray(obj)) {
    const newArr = obj.map(i => snakeToCamel(i));
    return newArr;
  } else {
    const newObj = {};
    Object.keys(obj).forEach(key => {
      const newKey = key.replace(/_\w/g, function(m) {
        return m[1].toUpperCase();
      });
      newObj[newKey] = snakeToCamel(obj[key]);
    });
    return newObj;
  }
}

export function camelToSnake(obj) {
  if(!isObject(obj) && !isArray(obj)) return obj;
  if(isArray(obj)) {
    const newArr = obj.map(i => camelToSnake(i));
    return newArr;
  } else {
    const newObj = {};
    Object.keys(obj).forEach(key => {
      const newKey = key.replace(/([A-Z])/g, function(m) {
        return `_${m.toLowerCase()}`;
      });
      newObj[newKey] = camelToSnake(obj[key]);
    });
    return newObj;
  }
}
